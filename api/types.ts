export interface IAnalyticsData {
  id: number;
  name: string;
  value: number;
}

export interface IAnalyticsDataCollection {
  data: IAnalyticsData[];
}

export interface IAnalyticsDataCollectionResponse {
  data: IAnalyticsData[];
}

export interface IAnalyticsDataResponse {
  id: number;
  name: string;
  value: number;
}