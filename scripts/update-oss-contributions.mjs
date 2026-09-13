#!/usr/bin/env node
/** Refresh the public OSS contribution feed used on the home page. */

import { writeFile } from 'node:fs/promises';

const username = process.env.GITHUB_USERNAME ?? 'myz21';
const limit = Number(process.env.OSS_CONTRIBUTION_LIMIT ?? 8);
const output = new URL('../public/data/oss-contributions.json', import.meta.url);

async function githubApi(path, params = {}) {
  const url = new URL(`https://api.github.com${path}`);
  url.search = new URLSearchParams(params);
  const token = process.env.GH_TOKEN ?? process.env.GITHUB_TOKEN;
  const response = await fetch(url, { headers: { Accept: 'application/vnd.github+json', 'User-Agent': 'myz21-portfolio-oss-feed', 'X-GitHub-Api-Version': '2022-11-28', ...(token ? { Authorization: `Bearer ${token}` } : {}) } });
  if (!response.ok) throw new Error(`GitHub API request failed: ${response.status} ${response.statusText}`);
  return response.json();
}

function repositoryName(item) { return item.repository_url.replace('https://api.github.com/repos/', ''); }

async function search(kind) {
  const result = await githubApi('/search/issues', { q: `author:${username} is:${kind}`, sort: 'created', order: 'desc', per_page: limit });
  return result.items;
}

async function pullRequest(item) {
  const repo = repositoryName(item);
  const detail = await githubApi(`/repos/${repo}/pulls/${item.number}`);
  return { repo, number: item.number, title: item.title, status: detail.merged_at ? 'merged' : detail.state, url: item.html_url, created_at: item.created_at };
}

function issue(item) {
  return { repo: repositoryName(item), number: item.number, title: item.title, status: item.state, url: item.html_url, created_at: item.created_at };
}

const pullRequests = await Promise.all((await search('pr')).map(pullRequest));
const issues = (await search('issue')).map(issue);
const feed = { updated_at: new Date().toISOString().replace(/\.\d{3}Z$/, 'Z'), pull_requests: pullRequests, issues };
await writeFile(output, `${JSON.stringify(feed, null, 2)}\n`);
console.log(`Updated ${output.pathname} with ${pullRequests.length} PRs and ${issues.length} issues.`);
