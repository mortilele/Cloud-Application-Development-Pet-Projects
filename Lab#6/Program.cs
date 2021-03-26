using Microsoft.Identity.Client;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.Graph;    
using Microsoft.Graph.Auth;

public class Program {
	private const string _clientId = "2e06b1ad-214c-485e-a903-c0d912a15afd";
	private const string _tenantId = "57081b5e-e66a-4993-8eaf-15b0b309293f";

	public static async Task Main(string[] args) {
		IPublicClientApplication app = PublicClientApplicationBuilder
									.Create(_clientId)
									.WithAuthority(AzureCloudInstance.AzurePublic, _tenantId)
									.WithRedirectUri("http://localhost")
									.Build();
		List<string> scopes = new List<string> { "user.read" };
		// AuthenticationResult result = await app
		// 	.AcquireTokenInteractive(scopes)
		// 	.ExecuteAsync();
		// Console.WriteLine($"Token:\t{result.AccessToken}");
		DeviceCodeProvider provider = new DeviceCodeProvider(app, scopes);
		GraphServiceClient client = new GraphServiceClient(provider);
		User myProfile = await client.Me.Request().GetAsync();
		Console.WriteLine($"Name:\t{myProfile.DisplayName}");
		Console.WriteLine($"AAD Id:\t{myProfile.Id}");
	}
}