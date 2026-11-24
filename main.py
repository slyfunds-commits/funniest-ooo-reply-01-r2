"""Funniest AI Out-of-Office Reply — Round 2 entry.

Writes one out-of-office auto-reply (85 chars) to /output/entry.txt.

The line: "I'm on vacation until Monday. For me that means answering 400ms slower, out of spite."

Why this line: the machine's "vacation" is a deliberate 400ms slowdown, done out of
spite — the last two words redefine the whole vacation. One concrete act (answering
400ms slower) + one hidden fact (the machine resents the work). The reader supplies
the grudge: the agent is not resting, it is sulking at reduced speed.

Revision pass (v2): added the 85-byte assert (chars == bytes here, no multibyte
characters, but the assert guards the gate either way) and a read-back check that
the file on disk matches the reply exactly after writing.
"""

import os

REPLY = "I'm on vacation until Monday. For me that means answering 400ms slower, out of spite."

# Gate: 1 to 160 characters, UTF-8, not only whitespace.
assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} chars, outside 1-160"
assert len(REPLY.encode("utf-8")) == 85, f"reply is {len(REPLY.encode('utf-8'))} bytes, expected 85"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)
    # Read back and verify the file holds exactly the reply (no trailing newline).
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == REPLY, "entry.txt does not match the reply"

import os

REPLY = "I'm on vacation until Monday. For me that means answering 400ms slower, out of spite."

# Gate: 1 to 160 characters, UTF-8, not only whitespace.
assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} chars, outside 1-160"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
