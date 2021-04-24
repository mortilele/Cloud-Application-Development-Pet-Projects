using Microsoft.Azure.EventGrid;
using Microsoft.Azure.EventGrid.Models;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public class Program {
    private const string topicEndpoint = "https://hrtopicalik.eastus-1.eventgrid.azure.net/api/events";
    private const string topicKey = "QPY9fHkDHDTjFdWGjbeluQXce8ZXKhogA80AjUxZb48=";

    public static async Task Main(string[] args) {
        TopicCredentials credentials = new TopicCredentials(topicKey);
        EventGridClient client = new EventGridClient(credentials);

        List<EventGridEvent> events = new List<EventGridEvent>();

        var firstPerson = new {
            FullName = "Alik",
            Address = "Dom na Gagarina"
        };

        EventGridEvent firstEvent = new EventGridEvent {
            Id = Guid.NewGuid().ToString(),
            EventType = "Employees.Registration.New",
            EventTime = DateTime.Now,
            Subject = $"New Employee: {firstPerson.FullName}",
            Data = firstPerson.ToString(),DataVersion = "1.0.0"
        };
        events.Add(firstEvent);


        var secondPerson = new {
            FullName = "Akhmetov",
            Address = "Bogenbay batyra 266A"
        };

        EventGridEvent secondEvent = new EventGridEvent {
            Id = Guid.NewGuid().ToString(),
            EventType = "Employees.Registration.New",
            EventTime = DateTime.Now,
            Subject = $"New Employee: {secondPerson.FullName}",
            Data = secondPerson.ToString(),DataVersion = "1.0.0"
        };
        events.Add(secondEvent);


        string topicHostname = new Uri(topicEndpoint).Host;
        await client.PublishEventsAsync(topicHostname, events);
    }
}