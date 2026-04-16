---
date: '2026-04-15T20:29:18-07:00'
draft: true
title: 'Automating Your Backports'
---

# Here's the rub

I joined npm about a little over a year ago, and never really had to deal with backporting. npm 11 was pretty well established at that point, and any dealings with npm 10 were really just dependency updates.

As we gear up for npm 12, I learned that we'll have to do quite a bit of backporting. In npm-land, that means manually cherry picking or creating commits and creating a duplicate PR, but against the other supported branches. I had little interest in doing that by hand.

# Here's the answer

This is where actions shine. In the main github repository, I was familiar with using labels to trigger backports. I wrote my own for npm. Any pull request with a matching backport version label should trigger the action. Also, adding a label to an already-merged pr would do the same. Boom - done. Now we can easily get all the needed backports to the appropriate branches.

# Specific Challenges

There was some tricky logic involved in the backporting. As a result of using `release-please` and `conventional commits`, we couldn't just grab the merge code and make one commit for all of it. Sure, in a squashed merge, that is the easy thing to do. In a PR where each commit needs to maintain its atomic commit and message - signaling to the changelog where and what each change is. The action code had to be smart about cherry-picking commits and maintaining the changelog-ability.

# Issues

We came across some quirks. First, the way it cherry-picks the commits means that they are their own commits in the other branch — if you signed the commit, you lose that validation.

Also, as a protective measure against infinite loops, workflows creating PRs don't trigger other workflows. I even made the workflow run the CI.yaml directly, and that works — the ci runs the tests correctly and succeeds — but the PR doesn't connect to that CI run, so there is no happy box in the PR saying it is good to merge. The best solution we have that is just to close and reopen the PR.

# Conclusion

In the end, I took a whole lot of drudgery out of the backporting process. I can't believe they've been doing it manually all these years! I wouldn't be surprised if it's my greatest npm contribution.
