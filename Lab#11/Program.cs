using Azure;
using Azure.Storage.Queues;
using Azure.Storage.Queues.Models;
using System;
using System.Text;
using System.Threading.Tasks;

public class Program {
    private const string storageConnectionString = "DefaultEndpointsProtocol=https;AccountName=asyncstoralik;AccountKey=coosQK9me23HIitpEVOgFLDlCd3i5zVGKe7+65sg5kcyaqXTltM49aZ6cLHpAyVATf/seperh+urVE6dlQcWDw==;EndpointSuffix=core.windows.net";
    private const string queueName = "messagequeue";

    public static async Task Main(string[] args) {
        QueueClient client = new QueueClient(storageConnectionString, queueName);
        await client.CreateAsync();
        
        Console.WriteLine($"---Account Metadata---");
        Console.WriteLine($"Account Uri:\t{client.Uri}");

        Console.WriteLine($"---Existing Messages---");

        int batchSize = 10;
        TimeSpan visibilityTimeout = TimeSpan.FromSeconds(2.5d);

        Response<QueueMessage[]> messages = await client.ReceiveMessagesAsync(batchSize, visibilityTimeout);
        foreach(QueueMessage message in messages?.Value) {
            Console.WriteLine($"[{message.MessageId}]\t{message.MessageText}");
            await client.DeleteMessageAsync(message.MessageId, message.PopReceipt);
        }

        Console.WriteLine($"---New Messages---");
        string greeting = "Hi, Developer! (Alik)";
        await client.SendMessageAsync(Convert.ToBase64String(Encoding.UTF8.GetBytes(greeting))); 
        Console.WriteLine($"Sent Message:\t{greeting}");
    }
}