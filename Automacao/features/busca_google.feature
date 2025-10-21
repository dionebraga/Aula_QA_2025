Feature: Pesquisa no Google
  Como um usuário da web
  Quero buscar por um termo no Google
  Para verificar se os resultados aparecem corretamente

  Scenario: Buscar Instituto Joga Junto
    Given que estou na página inicial do Google
    When eu pesquiso por "Instituto Joga Junto"
    Then o primeiro resultado deve conter "Instituto Joga Junto"
