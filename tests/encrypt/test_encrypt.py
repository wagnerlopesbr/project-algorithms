import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # the function "encrypt_message" should receive (string, int) as arguments
    with pytest.raises(TypeError) as e:  # type: ignore
        encrypt_message(123, "key")  # type: ignore
    assert str(e.value) == 'tipo inválido para key'  # type: ignore

    with pytest.raises(TypeError) as e:  # type: ignore
        encrypt_message("123", "key")  # type: ignore
    assert str(e.value) == 'tipo inválido para key'  # type: ignore

    with pytest.raises(TypeError) as e:  # type: ignore
        encrypt_message(123, 1)  # type: ignore
    assert str(e.value) == "tipo inválido para message"  # type: ignore

    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", 5) == "assem_eg"
    assert encrypt_message("message", 55) == "egassem"
    assert encrypt_message("newmessage", 7) == "ssemwen_ega"
    assert encrypt_message("anothernewmessage", 9) == "enrehtona_egassemw"

    assert encrypt_message("message", 2) == "egass_em"
    assert encrypt_message("message", 4) == "ega_ssem"
    assert encrypt_message("message", 44) == "egassem"
    assert encrypt_message("newmessage", 6) == "egas_semwen"
    assert encrypt_message("anothernewmessage", 8) == "egassemwe_nrehtona"
