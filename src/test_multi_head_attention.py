import torch

from src.multi_head_attention import MultiHeadAttention



# 假设ESM embedding

batch = 2
seq_len = 10
hidden_dim = 320


x = torch.randn(
    batch,
    seq_len,
    hidden_dim
)



attention = MultiHeadAttention(
    hidden_dim=320,
    num_heads=8
)



output = attention(x)



print("Input:")
print(x.shape)


print("Output:")
print(output.shape)