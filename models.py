from enum import Enum
from pydantic import BaseModel, conint


class LLMProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    TOGETHER = "together"


class LLMName(str, Enum):
    DAVINCI = "text-davinci-003"
    CLAUDE_1 = "claude-instant-1"
    CLAUDE_2 = "claude-2"
    GPT35 = "gpt-3.5-turbo"
    GPT4 = "gpt-4"
    LLAMA_2_70_B = "togethercomputer/llama-2-70b"
    LLAMA_2_70_B_CHAT = "togethercomputer/llama-2-70b-chat"


class LLM(Enum):
    OPENAI_GPT_3_5_TURBO = f"{LLMProvider.OPENAI}:{LLMName.GPT35}"
    OPENAI_GPT_4 = f"{LLMProvider.OPENAI}:{LLMName.GPT4}"
    OPENAI_TEXT_DAVINCI_003 = f"{LLMProvider.OPENAI}:{LLMName.DAVINCI}"
    ANTHROPIC_CLAUDE_1 = f"{LLMProvider.ANTHROPIC}:{LLMName.CLAUDE_1}"
    ANTHROPIC_CLAUDE_2 = f"{LLMProvider.ANTHROPIC}:{LLMName.CLAUDE_2}"
    TOGETHER_LLAMA_2_70_B = f"{LLMProvider.TOGETHER}:{LLMName.LLAMA_2_70_B}"
    TOGETHER_LLAMA_2_70_B_CHAT = f"{LLMProvider.TOGETHER}:{LLMName.LLAMA_2_70_B_CHAT}"


class LLMDetails(BaseModel):
    provider: LLMProvider
    name: LLMName
    max_tokens: conint(ge=1)
    default_max_tokens: conint(ge=1)
    max_query_length: conint(ge=1)


LLM_DETAILS = {
    LLM.OPENAI_TEXT_DAVINCI_003: LLMDetails(
        provider=LLMProvider.OPENAI,
        name=LLMName.DAVINCI,
        max_tokens=4096,
        default_max_tokens=200,
        max_query_length=400,
    ),
    LLM.OPENAI_GPT_3_5_TURBO: LLMDetails(
        provider=LLMProvider.OPENAI,
        name=LLMName.GPT35,
        max_tokens=4096,
        default_max_tokens=200,
        max_query_length=400,
    ),
    LLM.OPENAI_GPT_4: LLMDetails(
        provider=LLMProvider.OPENAI,
        name=LLMName.GPT4,
        max_tokens=8192,
        default_max_tokens=400,
        max_query_length=800,
    ),
    LLM.ANTHROPIC_CLAUDE_1: LLMDetails(
        provider=LLMProvider.ANTHROPIC,
        name=LLMName.CLAUDE_1,
        max_tokens=100_000,
        default_max_tokens=10_000,
        max_query_length=10_000,
    ),
    LLM.ANTHROPIC_CLAUDE_2: LLMDetails(
        provider=LLMProvider.ANTHROPIC,
        name=LLMName.CLAUDE_2,
        max_tokens=100_000,
        default_max_tokens=10_000,
        max_query_length=10_000,
    ),
    LLM.TOGETHER_LLAMA_2_70_B: LLMDetails(
        provider=LLMProvider.TOGETHER,
        name=LLMName.LLAMA_2_70_B,
        max_tokens=4096,
        default_max_tokens=300,
        max_query_length=400,
    ),
    LLM.TOGETHER_LLAMA_2_70_B_CHAT: LLMDetails(
        provider=LLMProvider.TOGETHER,
        name=LLMName.LLAMA_2_70_B_CHAT,
        max_tokens=4096,
        default_max_tokens=300,
        max_query_length=400,
    ),
}
