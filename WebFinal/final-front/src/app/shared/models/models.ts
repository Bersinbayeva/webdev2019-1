export interface ICategory {
  id: number;
  name: string;
}

export interface IProduct {
  id: number;
  name: string;
  price: number;
  count: number;
}

export interface IAuthResponse {
  token: string;
}
