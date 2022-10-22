from rgbayes.rgbayes import count_letters


def test_count_words() -> None:
    """Test word counting from a file."""
    assert count_letters("Hello") == 5