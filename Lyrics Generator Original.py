import time
import sys


def play_lyrics(lyrics, delay=0.35):
    """
    Displays song lyrics word by word with a specified delay.

    Args:
        lyrics (str): A multi-line string containing the song lyrics.
        delay (float): The time in seconds to wait between printing each word.
    """
    print("--- Starting Lyrics Player ---")
    print("Press Ctrl+C to exit")

    # The try-except block is the fail-safe. If the user presses Ctrl+C,
    # the KeyboardInterrupt is caught and the program exits gracefully.
    try:
        # Split the entire lyrics string into individual lines
        lines = lyrics.split("\n")

        for line in lines:
            # If the line is empty, print a blank line and pause
            if not line.strip():
                print()
                time.sleep(1)
                continue

            words = line.split()

            for word in words:
                # Print the word followed by a space
                print(word, end=" ")

                # Pause for the specified delay
                time.sleep(delay)

                sys.stdout.flush()

            # Print a new line after each line of lyrics is complete
            print()

    except KeyboardInterrupt:
        print("\nPlayer stopped by user.")

    print("\n--- Finishing Lyrics Player ---")


if __name__ == "__main__":
    # The lyrics for "Sunflower" by Post Malone and Swae Lee
    my_lyrics = """
Ay, ay, ay, ay (ooh)
Ooh, ooh, ooh, ooh (ooh)
Ay, ay
Ooh, ooh, ooh, ooh

Needless to say, I keep her in check
She was a bad-bad, nevertheless (yeah)
Callin' it quits now, baby, I'm a wreck (wreck)
Crash at my place, baby, you're a wreck (wreck)

Needless to say, I'm keeping her in check
She was all bad-bad, nevertheless
Callin' it quits now, baby, I'm a wreck
Crash at my place, baby, you're a wreck

Thinkin' in a bad way, losin' your grip
Screamin' at my face, baby, don't trip
Someone took a big L, don't know how that felt
Lookin' at you sideways, party on tilt

Ooh-ooh-ooh
Some things you just can't refuse
She wanna ride me like a cruise
And I'm not tryna lose

Then you're left in the dust
Unless I stuck by ya
You're the sunflower
I think your love would be too much
Or you'll be left in the dust
Unless I stuck by ya
You're the sunflower
You're the sunflower

Every time I'm leavin' on you (ooh)
You don't make it easy, no (no, no)
Wish I could be there for you
Give me a reason to, oh (oh)

Every time I'm walkin' out
I can hear you tellin' me to turn around
Fightin' for my trust and you won't back down
Even if we gotta risk it all right now, oh (now)

I know you're scared of the unknown ('known)
You don't wanna be alone (alone)
I know I always come and go (and go)
But it's out of my control

And you'll be left in the dust
Unless I stuck by ya
You're the sunflower
I think your love would be too much

Or you'll be left in the dust
Unless I stuck by ya
You're the sunflower
You're the sunflower (yeah)
    """

    # You can change the delay here. A smaller number means faster words.
    word_delay = 0.30  # seconds

    # Run the lyrics player with the example lyrics and delay
    play_lyrics(my_lyrics, word_delay)
