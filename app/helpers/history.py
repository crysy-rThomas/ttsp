def format_history(messages):
    fommated_SUA_messages = []
    for message in messages:
        fommated_SUA_messages.append({
            "role": message.role,
            "content": message.content,
        })
    
    return fommated_SUA_messages