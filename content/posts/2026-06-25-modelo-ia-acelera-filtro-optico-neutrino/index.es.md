+++
title = "Modelo de IA acelera 700 veces la simulación de filtros ópticos para detectores de neutrinos que ayudan a estudiar el universo"
subtitle = "Desarrollada en la UNIFAL-MG, la herramienta combina las leyes de la física y el aprendizaje automático para apoyar a DUNE - experimento internacional de detección de neutrinos "
date = "2026-06-25"
#dateFormat = "2006-01-02" # This value can be configured for per-post date formatting
author = "Rafael Martins da Silva Afeto"
authorTwitter = "" #do not include @
cover = "modelo-IA-para-filtro-optico-detector-neutrinos-1.jpg"
coverCaption = "Entorno de desarrollo del proyecto, con códigos en Python y gráficos de entrenamiento de la red neuronal aplicada a la óptica de filtros multicapa. (Imagen: Archivo/Mateus Rodrigues)"
tags = ["Aprendizaje Automático", "Filtro", "Inteligencia Artificial", "Neutrinos", "Programa de Posgrado en Física", "Projeto +Ciência", "Proyecto DUNE", "UNIFAL-MG"]
categories = ["Física", "Tecnología"]
keywords = ["simulación de filtros ópticos", "aprendizaje automático física", "detector de neutrinos", "experimento DUNE", "inteligencia artificial UNIFAL"]
description = "Investigadores de la UNIFAL-MG desarrollaron un modelo de aprendizaje automático que, con pocos datos reales, logró generar simulaciones ópticas de filtros usados en la captura de la señal de neutrinos. La solución resultó más precisa y hasta 700 veces más rápida que el método tradicional de simulación."
showFullContent = false
readingTime = false
hideComments = false
+++

Investigadores de la UNIFAL-MG desarrollaron un modelo de aprendizaje automático que, con pocos datos reales, logró generar simulaciones ópticas de filtros usados en la captura de la señal de neutrinos. La solución resultó más precisa y hasta 700 veces más rápida que el método tradicional de simulación.

El estudio formó parte de la maestría de Mateus Jesus de Oliveira Rodrigues, dirigida por el profesor Anibal Thiago Bezerra, en el [Programa de Posgrado en Física (PPGF)](https://www.unifal-mg.edu.br/ppgf/), y colabora con el experimento internacional [DUNE (Deep Underground Neutrino Experiment)](https://www.dunescience.org/), del cual la UNIFAL-MG es una de las instituciones brasileñas participantes.

{{< grid-gallery >}}
  {{< grid-item src="Mateus-Jesus-de-Oliveira-Rodrigues-1.jpg" alt="Mateus Jesus de Oliveira Rodrigues – investigador/autor del estudio. (Foto: Archivo Personal)" >}}
  {{< grid-item src="Anibal-Bezerra.jpg" alt="Anibal Thiago Bezerra – profesor/director del estudio. (Foto: Archivo Personal)" >}}
{{< /grid-gallery >}}

Un desafío inicial en el desarrollo de la investigación, titulada Aprendizaje automático en la detección de neutrinos de supernovas, fue la escasez de datos. Los investigadores tenían pocas curvas reales para entrenar el modelo. Como explica Anibal Bezerra, los sistemas de aprendizaje automático suelen exigir un gran volumen de datos y el material disponible habría sido insuficiente.

Para sortear esta limitación, la solución fue entrenar el modelo en dos etapas. Primero, el equipo utilizó 500 curvas generadas por el método convencional, el TMM (Transfer Matrix Method), que usa ecuaciones de la física para describir cómo la luz atraviesa los filtros. Estas curvas no reproducen con fidelidad la respuesta óptica del filtro real, pero le dan al modelo una base amplia para aprender. A continuación, las mediciones reales entraron en escena para calibrar esa base y mostrarle a la inteligencia artificial los detalles que el modelo matemático (TMM) no tenía.

El equipo también incorporó la física al propio modelo, denominado CPIGAN (Conditional Physics Informed Generative Adversarial Networks). “La parte ‘physics informed’ resalta el hecho de que les enseñamos la física detrás de la respuesta óptica a los modelos generativos adversariales condicionales, las CGAN”, explica Anibal Bezerra.

Como destaca el investigador, los filtros ópticos son capas de materiales diferentes que, apiladas, filtran la luz que incide sobre ellas y pueden dejar pasar solo algunas longitudes de onda específicas. Es mediante este filtrado riguroso que actúan como la “puerta de entrada” a las ARAPUCAS – trampas gigantes diseñadas para capturar el brillo de los neutrinos.

Convencionalmente, la simulación de estos componentes se hace con el TMM, pero, como explica el profesor, este método es una aproximación. “El método trata las interfaces entre los materiales como si fueran perfectas; sería el análogo óptico de ‘ignore la fricción’ en los problemas de mecánica”, argumenta.

Así, el CPIGAN se convierte en un modelo de red neuronal capaz de reproducir los resultados de transmisión óptica de filtros reales. “Además, son modelos mucho más rápidos computacionalmente que el TMM. Mostramos un aumento de más de 700 veces en la velocidad de obtención de las curvas de transmisión al comparar las CPIGAN con el TMM”, enfatiza Anibal Bezerra.

Según el investigador, se trata de un trabajo de física básica, orientado a desarrollar técnicas que puedan aplicarse en la creación de dispositivos. “Creemos que es un trabajo bastante relevante para la ingeniería de dispositivos ópticos, con diversas aplicaciones en la sociedad. Diseñamos un procedimiento de aprendizaje automático que puede extenderse a otros tipos de dispositivos y propiedades con aplicaciones directas en la industria óptica, por ejemplo”, resalta.

Los próximos pasos de la investigación ya están en marcha. El equipo busca desarrollar un modelo aún más general, capaz de aprender las propiedades de dispositivos con distintos números de capas de materiales. “Es un trabajo desafiante, para el cual ya estamos obteniendo algunos resultados bastante interesantes”, comparte el investigador.

La investigación contó con el apoyo de la [Coordinación de Perfeccionamiento de Personal de Nivel Superior (CAPES)](https://www.gov.br/capes/pt-br), que otorgó una beca de maestría al estudiante Mateus Rodrigues.

Visita la [página de la UNIFAL-MG](https://jornal.unifal-mg.edu.br/modelo-de-ia-acelera-em-700-vezes-a-simulacao-de-filtros-opticos-para-detectores-de-neutrinos-que-ajudam-a-estudar-o-universo/) para acceder al texto original completo.
