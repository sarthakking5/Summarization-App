import os
import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from langchain.schema import Document
from urllib.parse import urlparse, parse_qs

load_dotenv()

##streamlit app
st.set_page_config(page_title="LangChain: Summarize Text from YT or Website")
st.title('LangChain: Summarize Text From YT or Website')
st.subheader('Summarize URL')

## Get the Groq API KEY
with st.sidebar:
    groq_api_key=st.text_input("Groq API Key",value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

## Gemma model Using Groq API
llm=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt=PromptTemplate(template=prompt_template,input_variables=['text'])

def get_youtube_transcript_docs(url: str):
    try:
        video_id = parse_qs(urlparse(url).query).get('v', [None])[0]
        if not video_id:
            return []

        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id=video_id)

        full_text = "\n".join([snippet.text for snippet in fetched])
        return [Document(page_content=full_text)]
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        st.warning(f"No transcript available: {e}")
        return []
    except Exception as e:
        st.error(f"Failed to fetch YouTube transcript: {e}")
        return []

if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Waiting..."):
                print("URL being loaded:", generic_url)
                ## Loading the website data
                if 'youtube.com' in generic_url:
                    docs=get_youtube_transcript_docs(generic_url)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    docs=loader.load()

                ## Initialize Chain for Summarization
                if docs:
                    chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                    output_summary=chain.run(docs)
                    st.success(output_summary)
                else:
                    st.warning('No transcript data available to summarize')
        except Exception as e:
            st.exception(e)
