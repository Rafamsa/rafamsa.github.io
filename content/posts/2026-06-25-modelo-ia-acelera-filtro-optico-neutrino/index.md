+++
title = "Modelo de IA acelera em 700 vezes a simulação de filtros ópticos para detectores de neutrinos que ajudam a estudar o universo"
subtitle = "Desenvolvida na UNIFAL-MG, a ferramenta combina leis da física e aprendizado de máquina para apoiar o DUNE - experimento internacional de detecção de neutrinos "
date = "2026-06-25"
#dateFormat = "2006-01-02" # This value can be configured for per-post date formatting
author = ""
authorTwitter = "" #do not include @
cover = "modelo-IA-para-filtro-optico-detector-neutrinos-1.jpg"
#Ambiente de desenvolvimento do projeto, com códigos em Python e gráficos de treinamento da rede neural aplicada à óptica de filtros multicamadas. (Imagem: Arquivo/Mateus Rodrigues)
tags = ["Aprendizado de Máquina", "Filtro", "Inteligência Artificial", "Neutrinos", "Programa de Pós-Graduação em Física", "Projeto +Ciência", "Projeto Dune", "UNIFAL-MG"]
keywords = ["", ""]
description = ""
showFullContent = false
readingTime = false
hideComments = false
+++

Pesquisadores da UNIFAL-MG desenvolveram um modelo de aprendizado de máquina que, com poucos dados reais, foi capaz de gerar simulações ópticas de filtros usados na captura do sinal de neutrinos. A solução se mostrou mais precisa e até 700 vezes mais rápida que o método tradicional de simulação.

O estudo fez parte do mestrado de Mateus Jesus de Oliveira Rodrigues, orientado pelo professor Anibal Thiago Bezerra, junto ao [Programa de Pós-Graduação em Física (PPGF)](https://www.unifal-mg.edu.br/ppgf/), e colabora com o experimento internacional [DUNE (Deep Underground Neutrino Experiment)](https://www.dunescience.org/), do qual a UNIFAL-MG é uma das instituições brasileiras participantes.

{{< grid-gallery >}}
  {{< grid-item src="Mateus-Jesus-de-Oliveira-Rodrigues-1.jpg" alt="Mateus Jesus de Oliveira Rodrigues – pesquisador/autor do estudo. (Foto: Arquivo Pessoal)" >}}
  {{< grid-item src="Anibal-Bezerra.jpg" alt="Anibal Thiago Bezerra – professor/orientador do estudo. (Foto: Arquivo Pessoal)" >}}
{{< /grid-gallery >}}

Um desafio inicial no desenvolvimento da pesquisa intitulada Aprendizado de máquina na detecção de neutrinos em supernovas foi a escassez de dados. Os pesquisadores tinham poucas curvas reais para treinar o modelo. Como explica Anibal Bezerra, os sistemas de aprendizado de máquina costumam exigir grande volume de dados e o material disponível seria insuficiente.

Para contornar essa limitação, a saída foi treinar o modelo em duas etapas. Primeiro, a equipe utilizou 500 curvas geradas pelo método convencional, o TMM (Transfer Matrix Method), que usa equações da física para descrever como a luz atravessa os filtros. Essas curvas não reproduzem com fidelidade a resposta óptica do filtro real, mas dão ao modelo uma base ampla para aprender. Em seguida, as medições reais entraram em cena para calibrar essa base e mostrar à inteligência artificial os detalhes que o modelo matemático (TMM) não possuía.

A equipe também incorporou física ao próprio modelo, nomeado de CPIGAN (Conditional Physics Informed Generative Adversarial Networks). “A parte ‘physics informed’ salienta o fato de ensinarmos a física por trás da resposta óptica aos modelos generativos adversariais condicionais, as CGANs”, explica Anibal Bezerra.

Conforme destaca o pesquisador, os filtros ópticos são camadas de materiais diferentes que, empilhados, filtram a luz que os atinge, podendo, deixar apenas alguns comprimentos de onda específicos passarem. É por meio dessa filtragem rigorosa que eles atuam como a “porta de entrada” para as ARAPUCAS – armadilhas gigantes projetadas para capturar o brilho dos neutrinos.

Convencionalmente, a simulação para estes componentes é feita pelo TMM, mas como o professor explica, esse método é uma aproximação. “O método trata as interfaces entre os materiais como sendo perfeitas, seria o análogo ótico para o ‘ignore o atrito’ nos problemas de mecânica”, argumenta.

O CPIGAN se torna um modelo de rede neural capaz de reproduzir os resultados de transmissão óptica de filtros reais. “Adicionalmente, são modelos muito mais rápidos computacionalmente que os TMM. Mostramos um aumento na velocidade de obtenção das curvas de transmissão de mais de 700 vezes ao compararmos as CPIGAN com o TMM”, enfatiza Anibal Bezerra.

Segundo o pesquisador, trata-se de um trabalho de física básica, voltado a desenvolver técnicas que possam ser aplicadas na criação de dispositivos. “Acreditamos que seja um trabalho bastante relevante para a engenharia de dispositivos óticos, com diversas aplicações na sociedade. Desenhamos um procedimento de aprendizado de máquina que pode ser estendido para outros tipos de dispositivos e propriedades com aplicações diretas na indústria óptica, por exemplo”, ressalta.

Os próximos passos da pesquisa já estão em andamento. A equipe busca desenvolver um modelo ainda mais geral, capaz de aprender as propriedades de dispositivos com diversos números de camadas de materiais. “É um trabalho desafiador, para o qual já estamos obtendo alguns resultados bastante interessantes”, compartilha o pesquisador.

A pesquisa contou com o apoio da [Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES)](https://www.gov.br/capes/pt-br) na concessão de bolsa de mestrado ao discente Mateus Rodrigues.

Visite a [página da UNIFAL-MG](https://jornal.unifal-mg.edu.br/modelo-de-ia-acelera-em-700-vezes-a-simulacao-de-filtros-opticos-para-detectores-de-neutrinos-que-ajudam-a-estudar-o-universo/) para acessar o texto na íntegra.
