import datetime


def get_x(dfs):
    date_of_match_strings = dfs["Match"]["date"]
    birthday_strings = [birthday for birthday in dfs["Player"]["birthday"]]

    def player_vals(id):
        '''
        return a 38x1 array of the player's attributes in FIFA
        :param id: int64
        :return: np.array(float64)
        '''
        pass


    def age(date_of_match_strings, birthday_strings):
        match_d_splits = [i.split(" ")[0].split("-") for i in
                          date_of_match_strings]
        birthday_d_splits = [i.split(" ")[0].split("-") for i in
                             birthday_strings]
        match_dates = [datetime.date(int(i[0]), int(i[1]), int(i[2])) for i in
                       match_d_splits]
        birthday = [datetime.date(int(i[0]), int(i[1]), int(i[2])) for i in
                    birthday_d_splits]
        return (match_dates[0] - birthday[0]).days
