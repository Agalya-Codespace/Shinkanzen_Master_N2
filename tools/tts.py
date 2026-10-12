"""Read-aloud audio for listening scripts whose CD track is missing (Open JTalk, `pip install pyopenjtalk`).
Usage: python3 tools/tts.py tools/tts/a01.txt audio/chokai/a01.mp3
Script lines: "N: ..." narrator, "M: ..." man, "F: ..." woman, "M2:"/"F2:" second voices, "-" = pause.
Ordinary Japanese with kanji is fine: Open JTalk reads it with its own dictionary."""
import sys, subprocess, numpy as np, pyopenjtalk
VOICE = {"N": (2, 0.95), "M": (0, 1.0), "M2": (-3, 0.95), "F": (6, 1.0), "F2": (8, 1.05)}  # (half_tone, speed)
out, sr = [], 48000
def gap(sec): out.append(np.zeros(int(sr * sec), dtype=np.float32))
gap(0.5)
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"): continue
    if line == "-": gap(2.0); continue
    who, text = line.split(":", 1)
    ht, sp = VOICE[who.strip()]
    x, sr = pyopenjtalk.tts(text.strip(), half_tone=ht, speed=sp)
    out.append(x.astype(np.float32) / 32768.0); gap(0.6)
pcm = (np.clip(np.concatenate(out), -1, 1) * 32767).astype("<i2").tobytes()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(sr), "-ac", "1", "-i", "-", "-b:a", "64k", sys.argv[2]], input=pcm, check=True)
print("wrote", sys.argv[2])
