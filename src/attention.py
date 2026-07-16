import torch
import torch.nn as nn
import torch.nn.functional as F

class SelfAttention(nn.Module):

    def __init__(self, hidden_dim):
        super().__init__()

        self.hidden_dim = hidden_dim

        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)

    def forward(self,x):
        Q = self.q_proj(x)
        K = self.k_proj(x)
        V = self.v_proj(x)

        scores = torch.matmul(
            Q,
            K.transpose(-1, -2)
        )
        scores = scores / (self.hidden_dim ** 0.5)

        attention_weights = F.softmax(
            scores,
            dim=-1
        )
        output = torch.matmul(
            attention_weights,
            V
        )
        return output
