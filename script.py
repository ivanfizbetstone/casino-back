

for agent in  mongo.db.agents.find():
    basepath ="https://api-lonetm.k2net.io/api/v1/agents/"+agent['agent']+"/players/"+agent['agent']+"/Sessions "
