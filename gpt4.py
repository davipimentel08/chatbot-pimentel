# titulo
# campo de mensagem
# a cada mensagem enviada pelo usuario:
    # aparecer a mensagem que ele enviou
    # enviar a pergunta para uma IA respoder
    # mostrar a resposta da IA

# streamlitr --> apenas com python criar o backend e frontend
# iremos usar a IA OpenAI

import streamlit as st # importar o streamlit
from openai import OpenAI

modelo_ia = OpenAI(api_key='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')

st.write('# ChatBot Pimentel') # titulo do chatbot, a hashtag deixa o titulo maior

if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []


texto_usuario = st.chat_input('digite sua mensagem') # balao de texto com a mansagem
# arquivo = st.file_uploader('selecione um arquivo')

for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)

if texto_usuario: # so ira mostrar se tiver mensagem
    st.chat_message('user').write(texto_usuario) # mostrar a mensagem do usuario
    mensagem_usuario = {'role': 'user', 'content': texto_usuario}
    st.session_state['lista_mensagens'].append(mensagem_usuario)

    resposta_modelo = modelo_ia.chat.completions.create(messages=st.session_state['lista_mensagens'], model='gpt-4o')
    # print(resposta_ia)

    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message('assistant').write(resposta_ia) 
    mensagem_ia = {'role': 'assistant', 'content': resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)

# print(st.session_state['lista_mensagens'])
