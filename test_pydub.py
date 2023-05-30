from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("audio/001-051.wav", format="wav")

new = sound[:1*1000] + sound[3*1000:]
new.export("test_001-051p.wav", format="wav")

play(new)