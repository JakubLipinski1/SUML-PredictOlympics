import { TeamProbability } from "./TeamProbability";

export class Prediction{
    event_name:string;
    medal_type:string;
    top_teams: TeamProbability[];

    constructor(event_name:string, medal_type:string, top_teams:TeamProbability[])
    {
        this.event_name = event_name;
        this.medal_type = medal_type;
        this.top_teams = top_teams;
    }
}