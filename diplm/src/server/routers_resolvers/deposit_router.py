from src.database.db_manager import db
from src.server.router import Router
from src.database.models import BaseModelModify

class TaskRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(TaskRouter, self).__init__(name, model)
        # self.router.add_api_route('/get_data', get_data, methods=["get"])
        self.router.add_api_route('/get_all_data', self.get_all_data, methods=["get"])

    def get_all_data(self):
        res_list = db.execute(query=f"select * from Deposit "
                                    f"join ClientData ON ClientData.id = Deposit.ClientData_id "
                                    f"join Personal ON Personal.id = Deposit.Personal_id "
                                    f"join Item ON Item.id = Deposit.item_id "
                                    f"join ItemType ON ItemType.id = Item.type_id",
                              many=True)
        return self.get_models(res_list)

    def get_models(self, res_list) -> list:
        models = []
        if res_list:
            print(res_list)
            for res in res_list:
                print(res)
                continue
                models.append({
                    "item": res[0],
                    "clientdata": (res[1], res[2], res[3], res[4], res[5]),
                    "personal": (res[6], res[7], res[8], res[9]),
                    "metal": (res[10], res[11]),
                    "test": (res[12], res[13]),
                    "item_weight": (res[12], res[13])
                })
        return models


