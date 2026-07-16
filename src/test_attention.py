import torch
from src.attention import SelfAttention


x = torch.randn(
    2,
    10,
    320
)

attention = SelfAttention(320)

output = attention(x)

print(output.shape)
