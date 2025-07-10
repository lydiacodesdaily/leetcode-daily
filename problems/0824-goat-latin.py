# LeetCode 824 - Goat Latin
# https://leetcode.com/problems/goat-latin/

# ✅ Problem:
# You are given a sentence and asked to convert it to "Goat Latin" by the following rules:
# 1. If a word begins with a vowel (a, e, i, o, u), append "ma" to the end.
# 2. If a word begins with a consonant, remove the first letter, place it at the end, then add "ma".
# 3. Add one letter 'a' to the end of each word per its word index (starting at 1).
# Return the final transformed sentence.

# 📚 Pattern:
# String Manipulation

# 🔍 Key Insight:
# - Use .split() to process each word in the sentence
# - Apply the Goat Latin rules to each word based on its starting character
# - Append increasing number of 'a's by index (starting at 1)

# 🧠 Memory Hook:
# vowel → word + "ma"
# consonant → word[1:] + word[0] + "ma"
# + "a" * (index + 1)

# ✅ Time Complexity: O(n), where n = total characters
# ✅ Space Complexity: O(n), for result storage

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Define vowel set for fast lookup (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")

        # Split sentence into words
        words = sentence.split()
        result = []

        # Process each word with index
        for i, word in enumerate(words):
            if word[0] in vowels:
                # Starts with vowel → just add 'ma'
                goat_word = word + "ma"
            else:
                # Starts with consonant → move first letter to end + 'ma'
                goat_word = word[1:] + word[0] + "ma"

            # Add "a" repeated (i + 1) times
            goat_word += "a" * (i + 1)

            # Append transformed word
            result.append(goat_word)

        # Join all words to form the final Goat Latin sentence
        return " ".join(result)


# 🔄 Example Dry Run:
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaa oatGmaaa atinLmaaaa"
if __name__ == "__main__":
    sol = Solution()
    sentence = "I speak Goat Latin"
    print(sol.toGoatLatin(sentence))  # Output: "Imaa peaksmaa oatGmaaa atinLmaaaa"