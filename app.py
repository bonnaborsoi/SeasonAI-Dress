from openai import OpenAI
import streamlit as st
import random

# Chama a API
def gerar_imagem(estilo, cor, paleta, tipo):
    chave = ''
    
    client = OpenAI(
        organization='',
        api_key=chave
    )
    
    prompt = f"{'a' if estilo.lower() in ['a', 'e', 'i', 'o', 'u'] else 'an'} {cor} {estilo.lower()} feminine {tipo.lower()} hanging in display, white background. Single outfit in the '{paleta}' color palette. Photorealistic."

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    image_url = response.data[0].url
    
    return image_url

# Interface utilizando o streamlit

# Título e descrição
st.title("SeasonAI Dress")
st.markdown('''
            :rainbow[Bem-vinda ao SeasonAI Dress, sua plataforma de geração de looks que oferece uma experiência única e personalizada com base na sua paleta de cores pessoal] :dress: ''')
st.divider()

# Box das paletas
st.subheader('Paletas de cores:')

with st.container(height=350):
    st.image('images\\winter.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image('images\\spring.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image('images\\summer.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image('images\\autumn.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

#  Caixas de seleção
st.divider()
st.subheader('Escolha seu look!')
estilo = st.selectbox("Selecione o estilo da roupa:", ['Elegante', 'Casual', 'Clássico', 'Romântico', 'Criativo','Qualquer'])
cor = st.selectbox("Selecione a cor da roupa:", ['Vermelho', 'Azul', 'Verde', 'Amarelo', 'Rosa', 'Roxo', 'Marrom', 'Cinza', 'Preto', 'Branco', 'Qualquer'])
paleta = st.selectbox("Selecione a paleta da roupa:", [ 'Inverno Profundo', 'Inverno Frio', 'Inverno Brilhante','Primavera Brilhante', 'Primavera Quente', 'Primavera Clara','Verão Claro', 'Verão Frio', 'Verão Suave', 'Outono Suave','Outono Quente', 'Outono Profundo', 'Qualquer' ])
tipo = st.selectbox("Selecione o tipo da roupa:", ['Vestido', 'Top e saia', 'Blusa e calça', 'Qualquer'])

# Traduz pro inglês (interface está em português)
estilos = ['Elegant', 'Casual', 'Classic', 'Romantic', 'Creative']
cores = ['Red', 'Blue', 'Green', 'Yellow', 'Pink', 'Purple', 'Brown', 'Gray', 'Black', 'White']
paletas = ['Deep Winter', 'True Winter', 'Clear Winter', 'Clear Spring', 'True Spring', 'Light Spring', 'Light Summer', 'True Summer', 'Soft Summer', 'Soft Autumn', 'True Autumn', 'Deep Autumn']
tipos = ['Dress', 'Top and skirt', 'Blouse and pants']

# Botão para gerar output
if st.button("Gerar Outfit"):
    if estilo == 'Qualquer':
        estilo = random.choice(estilos)
    if cor == 'Qualquer':
        cor = random.choice(cores)
    if paleta == 'Qualquer':
        paleta = random.choice(paletas)
    if tipo == 'Qualquer':
        tipo = random.choice(tipos)
    
    if estilo == 'Elegante':
        estilo = 'Elegant'
    elif estilo == 'Clássico':
        estilo = 'classic'
    elif estilo == 'Romântico':
        estilo = 'Romantic'
    elif estilo == 'Criativo':
        estilo = 'Creative'
   
    if cor == 'Vermelho':
        cor = 'Red'
    elif cor == 'Azul':
        cor = 'Blue'
    elif cor == 'Verde':
        cor = 'Green'
    elif cor == 'Amarelo':
        cor = 'Yellow'
    elif cor == 'Rosa':
        cor = 'Pink'
    elif cor == 'Roxo':
        cor = 'Purple'
    elif cor == 'Marrom':
        cor = 'Brown'
    elif cor == 'Cinza':
        cor = 'Gray'
    elif cor == 'Preto':
        cor = 'Black'
    elif cor == 'Branco':
        cor = 'White'
    
    if paleta == 'Inverno Profundo':
        paleta = 'Deep Winter'
    elif paleta == 'Inverno Frio':
        paleta = 'True Winter'
    elif paleta == 'Inverno Brilhante':
        paleta = 'Clear Winter'
    elif paleta == 'Primavera Brilhante':
        paleta = 'Clear Spring'
    elif paleta == 'Primavera Quente':
        paleta = 'True Spring'
    elif paleta == 'Primavera Clara':
        paleta = 'Light Spring'
    elif paleta == 'Verão Claro':
        paleta = 'Light Summer'
    elif paleta == 'Verão Frio':
        paleta = 'True Summer'
    elif paleta == 'Verão Suave':
        paleta = 'Soft Summer'
    elif paleta == 'Outono Suave':
        paleta = 'Soft Autumn'
    elif paleta == 'Outono Quente':
        paleta = 'True Autumn'
    elif paleta == 'Outono Profundo':
        paleta = 'Deep Autumn'
    
    if tipo == 'Vestido':
        tipo = 'Dress'
    elif tipo == 'Top e saia':
        tipo = 'Top and skirt'
    elif tipo == 'Blusa e calça':
        tipo = 'Blouse and pants'
    
    image_url = gerar_imagem(estilo, cor, paleta, tipo)
    st.image(image_url, caption='Outfit Gerado', use_column_width=True)
