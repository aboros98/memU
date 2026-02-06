try:
    from memu._core import hello_from_bin
except ImportError:
    # Rust extension not available (cross-platform or pure Python install)
    def hello_from_bin():
        return "Hello from Python fallback!"


def _rust_entry() -> str:
    return hello_from_bin()
