import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IAuthResponse, ICategory, IProduct} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getCategories(): Promise<ICategory[]> {
    return this.get('http://localhost:8000/api/categories/', {});
  }

  getProducts(category: ICategory): Promise<IProduct[]> {
    return this.get(`http://localhost:8000/api/categories/${category.id}/products/`, {});
  }

  createCategory(name: any): Promise<ICategory> {
    return this.post('http://localhost:8000/api/categories/', {
      name: name
    });
  }

  updateCategory(category: ICategory): Promise<ICategory> {
    return this.put(`http://localhost:8000/api/categories/${category.id}/`, {
      name: category.name
    });
  }

  deleteCategory(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/categories/${id}/`, {});
  }

  auth(login: any, password: any): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {
    });
  }

}
