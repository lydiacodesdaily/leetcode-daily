# LeetCode 355 - Design Twitter
# https://leetcode.com/problems/design-twitter/

"""
✅ PROBLEM SUMMARY:
Design a simplified Twitter where users can:
- Post tweets
- Follow/unfollow other users  
- View 10 most recent tweets in their news feed (self + followees)

📚 PATTERN: HashMap + Min-Heap (Merge K Sorted Lists)

🎯 KEY INSIGHTS:
1. Each user's tweets are naturally sorted by time (append-only list)
2. News feed = merge K sorted lists (K = followed users + self)
3. Use heap to efficiently get top 10 without sorting everything
4. Negative timestamp in heap → max-heap behavior (most recent first)

⏱️ COMPLEXITY:
Time:  postTweet O(1) | follow O(1) | unfollow O(1) | getNewsFeed O(K)
Space: O(U + T + F) where U=users, T=tweets, F=follow relationships

🎓 INTERVIEW TIPS:
- Clarify: Can user see own tweets? YES
- Clarify: Can user follow themselves? NO
- Explain heap choice: "Only need top 10, heap is O(K) vs O(N log N) for sorting all"
- Mention: This is the 'Merge K Sorted Lists' pattern applied to tweets
"""

from collections import defaultdict
import heapq
from typing import List

# ============================================================================
# SOLUTION (Interview-Ready Code)
# ============================================================================

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId), ...]
        self.following = defaultdict(set)    # userId -> {followeeId, ...}
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # Min-heap: (-time, tweetId, userId, index)
        heap = []
        
        # Add user's own most recent tweet
        if self.tweets[userId]:
            time, tweetId = self.tweets[userId][-1]
            heapq.heappush(heap, (-time, tweetId, userId, len(self.tweets[userId]) - 1))
        
        # Add followees' most recent tweets
        for followeeId in self.following[userId]:
            if self.tweets[followeeId]:
                time, tweetId = self.tweets[followeeId][-1]
                heapq.heappush(heap, (-time, tweetId, followeeId, len(self.tweets[followeeId]) - 1))
        
        # Extract top 10 tweets
        feed = []
        while heap and len(feed) < 10:
            neg_time, tweetId, uid, idx = heapq.heappop(heap)
            feed.append(tweetId)
            
            # Add next older tweet from same user
            if idx > 0:
                time, tweetId = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-time, tweetId, uid, idx - 1))
        
        return feed
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

# ============================================================================
# INTERVIEW TALKING POINTS
# ============================================================================
"""
🗣️ HOW TO EXPLAIN YOUR APPROACH:

"I'll use a HashMap to track followers and tweets per user, and a min-heap 
to efficiently merge the most recent tweets from all followed users.

The key insight is that each user's tweets are already sorted by time since 
we append them chronologically. Getting the news feed becomes a 'Merge K 
Sorted Lists' problem where K is the number of followed users plus the user 
themselves.

I'll use a heap to track the most recent unprocessed tweet from each user. 
I pop the most recent tweet, add it to the result, then push the next tweet 
from that same user. This gives us the top 10 in O(K + 10 log K) time, which 
simplifies to O(K) since K is bounded by 500 users."

🎯 FOLLOW-UP QUESTIONS YOU MIGHT GET:

Q: "Why not just sort all tweets?"
A: "That would be O(N log N) where N is total tweets. With the heap approach, 
    we only process what we need - up to 10 tweets from at most K users, 
    giving us O(K) which is much better when users have many tweets."

Q: "What if we want to support 'unlike' or deleting tweets?"
A: "For unlike, we'd need to store tweet metadata. For deletion, I'd add a 
    'deleted' flag rather than removing from the list to keep indices stable, 
    then filter deleted tweets in getNewsFeed."

Q: "How would this scale to millions of users?"
A: "We'd need to paginate results, cache popular users' feeds, and possibly 
    use a distributed system. We could also pre-compute feeds for active users 
    and use fan-out on write for users with few followers."

Q: "Why use defaultdict instead of regular dict?"
A: "It avoids KeyError checks. If a user hasn't posted or followed anyone, 
    we get an empty list/set automatically. Cleaner code for interviews."
"""

# ============================================================================
# TEST CASES & DRY RUN
# ============================================================================

def test_twitter():
    """Test case from problem description"""
    twitter = Twitter()
    
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]
    
    print("✅ All tests passed!")

def test_edge_cases():
    """Additional edge cases to discuss"""
    twitter = Twitter()
    
    # Edge case: User follows themselves (should be ignored)
    twitter.follow(1, 1)
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    
    # Edge case: Unfollow non-existent follow relationship
    twitter.unfollow(1, 2)  # Should not crash
    
    # Edge case: User with no tweets
    assert twitter.getNewsFeed(999) == []
    
    # Edge case: More than 10 tweets
    for i in range(15):
        twitter.postTweet(1, i)
    feed = twitter.getNewsFeed(1)
    assert len(feed) == 10
    assert feed[0] == 14  # Most recent
    
    print("✅ All edge cases passed!")

"""
DRY RUN (Explain this in interview):

Initial: tweets={}, following={}, time=0

postTweet(1, 5):
  tweets={1: [(0,5)]}, time=1

getNewsFeed(1):
  heap=[(-0,5,1,0)]
  pop (-0,5,1,0) → feed=[5]
  return [5] ✓

follow(1, 2):
  following={1: {2}}

postTweet(2, 6):
  tweets={1:[(0,5)], 2:[(1,6)]}, time=2

getNewsFeed(1):
  heap=[(-1,6,2,0), (-0,5,1,0)]  ← user 1 and user 2's latest
  pop (-1,6,2,0) → feed=[6]      ← 6 is most recent
  pop (-0,5,1,0) → feed=[6,5]
  return [6,5] ✓
"""

# ============================================================================
# COMPARISON: Why This Beats Alternatives
# ============================================================================
"""
❌ Approach 1: Sort all tweets every time
   Code: tweets = all_tweets_from_user_and_followees()
         tweets.sort(key=lambda x: -x[0])
         return tweets[:10]
   Time: O(N log N) where N = total tweets
   Why worse: Wasteful when N >> 10

❌ Approach 2: Pre-compute feeds (fan-out on write)
   Code: On postTweet, update all followers' feeds
   Time: postTweet O(F) where F = # followers, getNewsFeed O(1)
   Why worse: Expensive for celebrities with millions of followers

✅ Our Approach: Heap (fan-out on read)
   Time: postTweet O(1), getNewsFeed O(K) where K ≤ 500
   Why better: Balanced - efficient for both reads and writes
"""

# ============================================================================
# RELATED PROBLEMS (Same Pattern)
# ============================================================================
"""
Master this pattern, ace these problems:

Heap + Merge K Lists:
- LC 23: Merge K Sorted Lists ⭐⭐⭐
- LC 373: Find K Pairs with Smallest Sums
- LC 378: Kth Smallest Element in Sorted Matrix
- LC 632: Smallest Range Covering Elements from K Lists

Design Problems:
- LC 146: LRU Cache (HashMap + Doubly Linked List)
- LC 380: Insert Delete GetRandom O(1)
- LC 1756: Design Most Recently Used Queue
"""

if __name__ == "__main__":
    test_twitter()
    test_edge_cases()