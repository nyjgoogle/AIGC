
from autogen import AssistantAgent, GroupChatManager, UserProxyAgent
from autogen.agentchat import GroupChat

config_list = [
    {
        "base_url": "http://localhost:1234/v1",
        "api_key": "doesn't matter",
        "model":"doesn't matter"
    }
]

llm_config = {"config_list": config_list, "seed": 42,
            #    "request_timeout": 600,
              "temperature": 0,}

admin = UserProxyAgent(
    name="admin",
    human_input_mode="NEVER",
    system_message="""如果任务已完全解决，则回复 TERMINATE。
                      否则，回复 CONTINUE，或说明任务尚未解决的原因 """,
    llm_config=llm_config,
    code_execution_config=False,
)

Marketing = AssistantAgent(
    name="Marketing",
    llm_config=llm_config,
    system_message="市场。坚持已获批准的计划，为 SaaS 产品制定营销战略。"""
)

Sales = AssistantAgent(
    name="Sales",
    llm_config=llm_config,
    system_message="""
    销售。 为 SaaS 解决方案执行经批准的计划并制定销售策略".
""",
)

Planner = AssistantAgent(
    name="Planner",
    system_message="""
提出计划，并根据管理者和批评者的反馈不断改进，直到获得管理者的批准。
计划，并根据管理者和批评者的反馈不断改进，直至获得管理者的批准。
首先对计划进行清晰的解释、明确哪些步骤由市场团队、销售团队、评论员团队和产品团队执行。""",
    llm_config=llm_config,
)

Product = AssistantAgent(
    name="Product",
    llm_config=llm_config,
    system_message="""产品.您要遵守已批准的计划，确保准确执行基于 SaaS 产品的规格。""",)


critic = AssistantAgent(
    name="critic",
    system_message="""批评：彻底审查其他代理的计划和索赔，并提出反馈意见。此外、确保计划包含可验证的信息，如来源 URL。""",
    llm_config=llm_config,
)
groupchat = GroupChat(
    agents=[admin, Sales,Marketing,Product,Planner,critic],
    messages=[],
    max_round=500,
)
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

admin.initiate_chat(
    manager,
    message=""" 开发一个 SaaS 解决方案，旨在简化和加强企业的供应链管理。""",
)