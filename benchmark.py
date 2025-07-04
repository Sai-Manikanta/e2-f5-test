# benchmark.py
import time
import soundfile as sf
from f5_tts.infer.api import F5TTSInference

def run_benchmark():
    model = F5TTSInference(model_name="F5TTS_v1_Base")

    ref_audio = "F5-TTS/assets/sample.wav"
    ref_text = "This is the reference transcription."
    gen_text = "Hello, welcome to the F5-TTS benchmark test."

    start_time = time.time()
    output_path = model.infer(
        ref_audio=ref_audio,
        ref_text=ref_text,
        gen_text=gen_text,
        return_path=True
    )
    end_time = time.time()

    duration_sec = sf.info(ref_audio).duration
    elapsed = end_time - start_time
    rtf = elapsed / duration_sec

    return {
        "latency_seconds": round(elapsed, 3),
        "rtf": round(rtf, 4),
        "output_file": output_path
    }
