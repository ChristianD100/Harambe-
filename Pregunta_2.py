{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM3mq3bCGkVGBITLJtDl+5i",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ChristianD100/Harambe-/blob/main/Pregunta_2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M9aKoeOK_939",
        "outputId": "3b744f5b-db2e-4f22-f930-e0d5912e04ce"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Por favor ingrese su nombre: Christian\n",
            "Hola, Christian! Encantado de conocerte.\n",
            "\n",
            "¿En qué te puedo ayudar, Christian?\n"
          ]
        }
      ],
      "source": [
        "def usuario():\n",
        "    nombre = input(\"Por favor ingrese su nombre: \")\n",
        "    print(f\"Hola, {nombre}! Encantado de conocerte.\")\n",
        "    print()\n",
        "    print(f\"¿En qué te puedo ayudar, {nombre}?\")\n",
        "\n",
        "usuario()"
      ]
    }
  ]
}
