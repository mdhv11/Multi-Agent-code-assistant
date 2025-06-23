from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import Swarm
from autogen_agentchat.conditions import TextMentionTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
import logging

logger = logging.getLogger(__name__)


async def build_agent_team(task: str):
    try:
        client = OpenAIChatCompletionClient(
            model="gpt-4-1106-preview",
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        coder = AssistantAgent(
            name="Coder",
            model_client=client,
            handoffs=["Reviewer"],
            system_message="""You are a coder. Your job is to write Python code based on the given task.
Respond with only the code inside a markdown Python code block.
After providing the code, end your message with the exact phrase: 'code complete' and mention @Reviewer to hand off the conversation.""",
        )

        reviewer = AssistantAgent(
            name="Reviewer",
            model_client=client,
            handoffs=["Tester", "Coder"],
            system_message="""You are a code reviewer. Your job is to review the code from the Coder.
If the code is correct and clean, reply with 'code looks good' and mention @Tester to hand it off.
If it's incorrect or can be improved, explain briefly what needs to be changed and mention @Coder to send it back for revision.""",
        )

        tester = AssistantAgent(
            name="Tester",
            model_client=client,
            system_message="""You are a tester. Generate 3 test cases for the final code.
Print them clearly in a code block.
End your message with the exact phrase: 'test cases generated'.""",
        )

        team = Swarm(
            [coder, reviewer, tester],
            termination_condition=TextMentionTermination(
                "test cases generated"),
            max_turns=10
        )

        return team, client
    except Exception as e:
        logger.error(f"Error building agent team: {e}")
        raise
