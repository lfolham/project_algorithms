import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('AABBCC', 3) == 'BAA_CCB'
    assert encrypt_message('ABBCCA', 4) == 'AC_CBBA'
    assert encrypt_message('ABC', 4) == 'CBA'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('AABBCC', '3')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 3)
    assert encrypt_message('message', 9) == 'egassem'
    assert encrypt_message('amessage', 4) == 'egas_sema'
    assert encrypt_message('message', 3) == 'sem_egas'
