from exercises.mutables import (
    bad_append,
    safe_append,
    bad_count,
    safe_count,
    bad_collect,
    safe_collect,
    bad_register,
    safe_register,
)


def test_bad_append_shared_state():
    # First call creates [1]
    assert bad_append(1) == [1]
    # Second call appends to the same default list -> [1, 2]
    assert bad_append(2) == [1, 2]


def test_safe_append_isolated():
    assert safe_append(1) == [1]
    assert safe_append(2) == [2]


def test_bad_count_shared_state():
    # Shared dict accumulates counts across calls
    assert bad_count("x") == {"x": 1}
    assert bad_count("x") == {"x": 2}


def test_safe_count_isolated():
    assert safe_count("x") == {"x": 1}
    assert safe_count("x") == {"x": 1}


def test_bad_collect_shared_state():
    assert bad_collect("a") == ["a"]
    assert bad_collect("b") == ["a", "b"]


def test_safe_collect_isolated():
    assert safe_collect("a") == ["a"]
    assert safe_collect("b") == ["b"]


def test_bad_register_shared_state():
    f1 = lambda: 1
    f2 = lambda: 2
    assert bad_register(f1) == [f1]
    assert bad_register(f2) == [f1, f2]


def test_safe_register_isolated():
    f1 = lambda: 1
    f2 = lambda: 2
    assert safe_register(f1) == [f1]
    assert safe_register(f2) == [f2]
