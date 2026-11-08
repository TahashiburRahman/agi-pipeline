class BasicEvaluator:
    """Structural check only; not a factuality or safety verifier."""
    def evaluate(self, result):
        if result is None:
            return False, "No result"
        if not result.success:
            return False, "Agent reported failure"
        if not result.output or not result.output.strip():
            return False, "Empty output"
        return True, "Non-empty successful output"
