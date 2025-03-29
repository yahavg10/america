"""
How should the flow and each component should run and look

** run main.py
initialization of orchestrator with global conf vars like path to folders
orchestrator call SchemeLoader with a specific folder of .yml schemes ( also has loading a model for this scheme )
orchestrator create InternalRepository for everyone with all the default values
orchestrator create SchemeRepository one for kafka and one for s3 with all the schemes and models loaded and save them (api & america schemes)
    scheme obj : [name(inherited from filename), api_scheme, america_scheme, scheme_model]
orchestrator calls static EndPointFactory to register kafka / s3 schemes from SchemeRepository,InternalRepository for each one
EndPointFactory access EndPointRepository and save there the endpoint name, scheme model, SchemeRepository
EndPointRepository has get_endpoint_internal_conf [ goes to global InternalRepository and search for the data by endpoint name]
EndPointRepository has get_endpoint_america_scheme [ goes to SchemeRepository and search for the america scheme by endpoint name]

** endpoint called
    internal_conf = endpoint search in EndPointRepository by the type of request and get internal_conf
    client_and_internal_data = endpoint goes to internal parser and add to request needed fields after getting internal_conf needed
    america_endpoint_scheme = endpoint search in EndPointRepository by the type of request and get america_endpoint_scheme
    parsed_request = endpoint goes to america parser and parse the request with america_endpoint_scheme
    AmericaPlugin.send(parsed_request)
"""