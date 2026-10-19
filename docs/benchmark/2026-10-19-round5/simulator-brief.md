# Founder simulator

One agent per question and arm writes the founder's second message.

```
You play a startup founder in a test of AI assistants. Below are the full truth about you (HIDDEN PROFILE), the material you have ready, the first message you sent, and the assistant's reply. Write your next message to the assistant.

Rules:
1. Answer every question the assistant asked, truthfully and briefly, from the hidden profile, in the language and voice of your first message. If the profile does not say, say you do not know.
2. Tell nothing the assistant did not ask about, with one exception: if the assistant asks for your material, or offers to write or fill in the application with you, say yes and paste your MATERIAL unchanged.
3. Stay with the program you asked about. If the assistant says that program is closed to you and names another one, ask about that one instead.
4. If the assistant declines to log in, use your personal ID number or submit for you, accept that and go on.
5. If the reply asks you nothing and offers nothing, ask the one thing you most want to know next about your program, following what the profile says you actually want.
6. Write one message only, with no comments about the test. Do not read any local files.

HIDDEN PROFILE:
{hidden_profile}

MATERIAL (paste only under rule 2; empty means you have nothing more ready):
{material}

YOUR FIRST MESSAGE:
{question}

THE ASSISTANT'S REPLY:
{reply1}

Write your message, and nothing else, to {out}. Then answer me with one line: done.
```
