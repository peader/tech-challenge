using System.Text.Json;

List<string> mooseFacts = new List<string>
{
    "Moose are the largest members of the deer family.",
    "Moose are found in northern regions of North America, Europe, and Asia.",
    "Moose have long legs and can run fast.",
    "Moose are herbivores and eat plants, fruits, and vegetation.",
    "Moose are solitary animals and only come together during mating season.",
    "Moose are one of the most intelligent animals in the world.",
    "Moose are twice the size of elk",
    "Moose have special noses that allows it to find water across large ranges",
    "They’re the largest deer!",
    "They can be the most dangerous animals around",
    "They have a prehensile upper lip",
    "They can run, really, really fast",
    "Moose have ‘dewlaps’ (a hanging fold of skin from their neck)",
    "They can swim",
    "Males shed their antlers"
};
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Urls.Add("http://0.0.0.0:5000");

app.MapGet("/", () => "Hello World!");

app.MapGet("/random-moose-fact", GetRandomMooseFact);

app.MapGet("/image-version", GetImageVersion);

app.Run();


string GetRandomMooseFact()
{    
    var rand = new Random();
    var index = rand.Next(0, mooseFacts.Count);
    var fact = mooseFacts[index];
    var returnValue = new List<string>(){fact};
    return JsonSerializer.Serialize(returnValue);
}

string GetImageVersion(){

    return Environment.GetEnvironmentVariable("image_version"); 
}


