<h1 align="center">ASCII Video Player in Terminal</h1>

<p align="center">
  <em>Play videos as colored ASCII art directly in your terminal using Python and OpenCV</em>
</p>

---

<h2>📜 Overview</h2>

<p>
This Python script reads a video file (<code>video.mp4</code>), converts each frame into colored ASCII art, and displays it live in your terminal. The playback speed is synchronized to the original video's FPS, with smart frame skipping to maintain smooth and accurate timing.
</p>

---

<h2>⚙️ How It Works</h2>

<ol>
  <li>
    <strong>Open Video</strong>: The script opens the video using <code>OpenCV (cv2)</code> and fetches its FPS to synchronize playback duration.
  </li>
  <li>
    <strong>Convert Frame to Grayscale</strong>: Each frame is converted to grayscale to simplify processing.
  </li>
  <li>
    <strong>Resize Frame</strong>: Frames are resized to a specified width (default 160 characters) with height adjusted by aspect ratio and half-block character height to maintain proportions.
  </li>
  <li>
    <strong>Map Pixels to ANSI Colors</strong>: Each pixel's brightness is mapped to a 256-color ANSI grayscale range (codes 232 to 255).
  </li>
  <li>
    <strong>Render Using Half-Block Characters</strong>: Two vertical pixels (top and bottom) are combined into a single character line using the Unicode '▀' (upper half block) with foreground and background ANSI colors to improve vertical resolution.
  </li>
  <li>
    <strong>Smart Frame Skipping</strong>: If the script lags behind real-time, it skips frames to catch up, keeping the playback duration accurate without displaying every frame.
  </li>
  <li>
    <strong>Clear Terminal & Display</strong>: Clears the terminal each frame and prints the colored ASCII frame.
  </li>
</ol>

---

<h2>🛠️ Usage</h2>

<pre><code>python ASCIIVidPlayerSkip.py
</code></pre>

Make sure:
<ul>
  <li>You have <code>video.mp4</code> in the same directory or modify the filename in the script accordingly.</li>
  <li>Python packages <code>opencv-python</code> and <code>numpy</code> are installed.</li>
  <li>Your terminal supports ANSI 256 colors.</li>
</ul>

---

<h2>📌 Important Notes</h2>

<ul>
  <li>Terminal rendering can be CPU-intensive; you can adjust <code>width</code> parameter in the <code>frame_to_ansi_half_block</code> function for performance vs. quality trade-off.</li>
  <li>This script works best on terminals with true color or 256-color support.</li>
  <li>Interrupt the playback anytime with <code>Ctrl+C</code>.</li>
</ul>

---

<h2>🔧 Script Highlights</h2>

<pre><code>def gray_to_ansi(pixel):
    return 232 + int(pixel / 235 * 23)

def frame_to_ansi_half_block(frame, width=160):
    ...
    # maps grayscale pixels to half-block characters with ANSI colors
</code></pre>

---

<h2>💡 Want to contribute?</h2>
<p>Feel free to fork this repo, submit issues, or open pull requests to improve the playback quality or add new features.</p>

---

<p align="center">Made with ❤️ by Kicock</p>
