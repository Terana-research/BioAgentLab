import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):

    def __init__(
            self,
            hidden_dim,
            num_heads
    ):
        super().__init__()

        self.hidden_dim = hidden_dim
        self.num_heads = num_heads

        self.head_dim = hidden_dim // num_heads

        self.q_proj =nn.Linear(
            hidden_dim,
            hidden_dim
        )
        self.k_proj = nn.Linear(
            hidden_dim,
            hidden_dim
        )
        self.v_proj = nn.Linear(
            hidden_dim,
            hidden_dim
        )

        self.out_proj = nn.Linear(
            hidden_dim,
            hidden_dim
        )

    def forward(self, x):

        batch_size = x.size(0)
        seq_len = x.size(1)
        Q = self.q_proj(x)
        K = self.k_proj(x)
        V = self.v_proj(x)

        Q = Q.view(
            batch_size,
            seq_len,
            self.num_heads,
            self.head_dim
        )
        K = K.view(
            batch_size,
            seq_len,
            self.num_heads,
            self.head_dim
        )
        V = V.view(
            batch_size,
            seq_len,
            self.num_heads,
            self.head_dim
        )
        Q = Q.transpose(1, 2)
        K = K.transpose(1, 2)
        V = V.transpose(1, 2)

        scores = torch.matmul(
            Q,
            K.transpose(-2, -1)
        )
        scores = scores / (self.head_dim ** 0.5)
        scores = F.softmax(scores, dim=-1)
        output = torch.matmul(
            scores,
            V
        )
        output = output.transpose(1, 2)
        output = output.contiguous().view(batch_size, seq_len, self.hidden_dim)

        output = self.out_proj(output)
        return output


