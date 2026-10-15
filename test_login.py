def concluir_login(forcar_erro):
    if forcar_erro:
        print("Erro forçado")
        return False

    print(
        "Iniciando o processo de login no sistema com "
        "credenciais válidas e aguardando o tempo de resposta "
        "do servidor..."
    )
    return True


def realizar_login(usuario, senha, forcar_erro):
    if not usuario:
        print("Usuário inválido")
        return False

    if senha is None:
        print("Senha vazia")
        return False

    return concluir_login(forcar_erro)


def test_verificar_login_valido():
    token_sessao = "abc123xyz"  # noqa: F841
    assert realizar_login(True, "123456", False)
