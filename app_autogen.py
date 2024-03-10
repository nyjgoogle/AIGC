import autogen
import os

os.environ["OPENAI_API_KEY"]="dummy_app_key"
llm_config = {
	"config_list":[{
			"model":"local-model",
            "api_key":"not-needed",
			"base_url":"http://127.0.0.1:1234/v1",			
			}]
}

llm_config={"config_list":[{"model":"llama2","api_key":os.environ["OPENAI_API_KEY"]}],
}

### 基于langchain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI(
    openai_api_key="anyValueYouLike",
    temperature=0,
    openai_api_base="http://localhost:1234/v1",
    #...any other options, read the langchain docs for more information if required
)

conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(),
    verbose=True
)

conversation.predict(input='Hi there !')
