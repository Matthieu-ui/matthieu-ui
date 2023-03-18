import time

# Define the frames of the animation
frames = [
 "  o  ",
 " o o ",
 "o   o",
 " o o ",
 "  o  ",
    "     ",
]

# Loop through the frames and display each one
for frame in frames:
    # Print the current frame
    print(frame, end="\r")

    # Wait for a short time before displaying the next frame
    time.sleep(0.1)

    # Save the current frame to a file
    with open(f"frame_{frame}.txt", "w") as f:
        f.write(frame)