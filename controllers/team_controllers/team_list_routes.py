from flask import render_template

from controllers.team_controllers import team

@team.route('/team-list' , methods=['GET'] , endpoint='team-list')
def team_list():
    return render_template('staff/team-list.html')