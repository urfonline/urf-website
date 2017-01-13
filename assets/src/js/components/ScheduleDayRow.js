import React from 'react';
import cx from 'classnames';
import moment from 'moment';
import ScheduleSlot from './ScheduleSlot';
import momentInternal from '../hoc/MomentInterval';
import { momentWeekDayMonday, slotIsOnAt } from '../utils/schedule';

function ScheduleDayRow(props) {
  const { shows, slots, calculateWidth } = props;

  if (slots === undefined) {
    return (<div>Nothing is scheduled.</div>);
  }

  const isToday = props.day === momentWeekDayMonday(props.momentInterval);

  return (
    <div className={cx('ScheduleRow', props.className)}>
      <div className="ScheduleRow__inner">
        <div className="ScheduleRow__slots">
          {slots.map((slot, index) => {
            const momentFrom = moment(slot.from_time);
            const momentTo = moment(slot.to_time);
            const fromTimeFormatted = momentFrom.format('hh:mm');
            const toTimeFormatted = momentTo.format('hh:mm');
            const timeKey = `${fromTimeFormatted}:${toTimeFormatted}`;
            const isOnAir = isToday &&
              slotIsOnAt(slot, props.momentInterval, index / (slots.length - 1));
            return (
              <ScheduleSlot
                key={timeKey}
                slot={slot}
                shows={shows}
                index={index}
                onAir={isOnAir}
                calculateWidth={calculateWidth}
              />
            );
          })}
        </div>
      </div>
    </div>
  );
}

ScheduleDayRow.propTypes = {
  momentInterval: React.PropTypes.object.isRequired,
  calculateWidth: React.PropTypes.func.isRequired,
  day: React.PropTypes.number.isRequired,
  className: React.PropTypes.string,
  slots: React.PropTypes.array.isRequired,
  shows: React.PropTypes.object.isRequired,
};

ScheduleDayRow.defaultProps = {
  className: '',
};


export default momentInternal({ interval: 60000 }, ScheduleDayRow);
