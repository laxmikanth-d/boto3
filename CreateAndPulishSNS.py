import boto3


def main():
    # Create topiic
    client = boto3.client('sns')
    topic = client.create_topic(Name='SNSAutomate',
                                Attributes={
                                    'DisplayName': 'SnsDisplay'
                                })

    snsArn = topic['TopicArn']

    response = client.publish(
        TopicArn = snsArn,
        Message = 'Hello World!'
    )

    # list_subscriptions = client.list_subscriptions_by_topic(
    #     TopicArn=snsArn
    # )

    # print(list_subscriptions)

    # subscription = client.subscribe(TopicArn=snsArn,
    #                                Protocol='email',
    #                                Endpoint='xx@gmail.com',
    #                                ReturnSubscriptionArn = True)

    # client.subscribe(TopicArn=snsArn,
    #                                Protocol='email',
    #                                Endpoint='xx2@gmail.com',
    #                                ReturnSubscriptionArn = True)
    # print(subscription)


if __name__ == "__main__":
    main()
