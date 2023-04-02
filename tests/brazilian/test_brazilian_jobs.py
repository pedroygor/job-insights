from src.pre_built.brazilian_jobs import read_brazilian_file

PATH = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():

    mock = [
        {"salary": "2000", "title": "Maquinista", "type": "trainee"},
        {"salary": "3000", "title": "Motorista", "type": "full time"},
        {
            "salary": "4000",
            "title": "Analista de Software",
            "type": "full time",
        },
        {
            "salary": "1700",
            "title": "Assistente administrativo",
            "type": " full time",
        },
        {
            "salary": "1400",
            "title": "Auxiliar administrativo",
            "type": " full time",
        },
        {
            "salary": "1400",
            "title": "Auxiliar usinagem",
            "type": " full time",
        },
        {
            "salary": "1400",
            "title": "Auxiliar de padaria",
            "type": " full time",
        },
        {
            "salary": "1400",
            "title": "Analista Contábil",
            "type": " full time",
        },
        {
            "title": "Gerente comercial",
            "salary": "5000",
            "type": " full time",
        },
        {
            "title": "Analista de Departamento Pessoal",
            "salary": "4000",
            "type": " full time",
        },
        {
            "title": "Esportista de Futebol profissional",
            "salary": "50000",
            "type": " full time",
        },
        {
            "salary": "4000",
            "title": "Analista de crédito",
            "type": " full time",
        },
        {
            "salary": "3000",
            "title": "Pessoa Programadora",
            "type": " full time",
        },
        {"title": "Ux Designer", "salary": "3000", "type": " full time"},
        {
            "salary": " 1400",
            "title": "Auxiliar de manutenção",
            "type": " full time",
        },
    ]

    assert read_brazilian_file(PATH) == mock
