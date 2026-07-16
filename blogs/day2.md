Input:

(batch, seq, hidden)

↓

QKV projection

(batch, seq, hidden)

↓

split heads

(batch, head, seq, head_dim)

↓

Attention

(batch, head, seq, seq)

↓

merge heads

(batch, seq, hidden)