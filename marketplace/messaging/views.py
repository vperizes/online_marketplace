from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from .models import Messages
from .forms import MessageForm


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    # if you're the owner of the item then redirect (can't have a message with yourself)
    if item.created_by == request.user:
        return redirect("dashboard:index")

    conversations = Messages.objects.filter(item=item).filter(
        members__in=[request.user.id]
    )

    # if a convo exists then redirect to that convo
    if conversations:
        pass  # redirect to conversation

    # check if message form has been submited
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            # create new conversation
            conversation = Messages.objects.create(item=item)
            # add person sending and recieving message to members list
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            # save conversation
            conversation.save()

            # now create message within conversation
            conversation_msg = form.save(commit=False)
            # set reference to above conversation
            conversation_msg.conversation = conversation
            conversation_msg.created_by = request.user
            conversation_msg.save()

            return redirect("item:detail", pk=item_pk)

    # if request is not post then create an empty form
    else:
        form = MessageForm()

    return render(
        request,
        "messaging/new_message.html",
        {
            "form": form,
        },
    )
